from django import template

register = template.Library()

@register.filter(expects_localtime= True)
def date_splitter_1(date,separator='-'):
    #import ipdb; ipdb.set.trace()
    return date.strftime(f'%d{separator}%m{separator}%Y')


@register.filter
def starrate(rating):
    html = '<fieldset class="rating">'
    for i in range (5):
        active = None
        if rating > i:
            active = 'style="color: #FFD700;"'
        html += f'''
            <input type="radio" id="star{i}" name="rating" value="{i}" /><label class = "full" {active}"for="star{i}" title="Awesome - 5 stars"></label>
            <input type="radio" id="starhalf" name="rating" value="half" /><label class="half" {active} for="starhalf" title="Pretty good - 0.5 stars"></label>
            '''
    html +='</fieldset>'
    return html
