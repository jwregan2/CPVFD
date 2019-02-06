Jekyll::Hooks.register [:pages, :documents], :pre_render do |side, payload|  # documents are collections, and collections include also posts
  base = side.path.split("/")[0...-1]
  payload["base"] = base.join("/") + "/"
end
