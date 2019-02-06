#!/bin/sh



err () {
  curl -X POST --data-urlencode 'payload={"attachments": [{"color": "#cc3333", "text": "Coordinated Attack Results production site build failed!"}]}' https://hooks.slack.com/services/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
  exit 1
}

echo "******** Building Jekyll site ********"
bundle exec jekyll build --config "_config.yml,_config.prod.yml" -t || err
echo "******** Uploading to S3 ********"
LC_ALL=en_US.UTF-8 aws s3 sync _site/ s3://ulfirefightersafety.org/private/coordinated-attack/ --acl public-read || err
echo S3 sync status: $?
echo "******** Invalidating CDN ********"
aws cloudfront create-invalidation --distribution-id E1TEROGZLQ0XZS --paths /private/coordinated-attack/\* || err
echo "******** Send build notification ********"
curl -X POST --data-urlencode 'payload={"attachments": [{"color": "#36a64f", "text": "Coordinated Attack Results production site build AOK! <https://ulfirefightersafety.org/private/coordinated-attack/index.html>"}]}' https://hooks.slack.com/services/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
