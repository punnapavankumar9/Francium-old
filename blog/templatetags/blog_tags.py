from django import template
register = template.Library()

@register.simple_tag
def get_image_url(posts):
    x = posts[0]
    url = x.author.profile.image.url
    return url