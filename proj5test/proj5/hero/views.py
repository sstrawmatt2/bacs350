from django.views.generic import TemplateView

from hero.models import Superhero

class HeroView(TemplateView):
    template_name="hero.html"
    
#    def get_context_data(self, **kwargs):
#        heroes = Superhero.objects.all()
#        return {
#            'title': 'Superhero Profile',
#            'heroes': heroes, 
#        }
    
    def get_context_data(self, **kwargs):
        id = kwargs.get('identity', 'Hulk')
        return{'hero': id, 'css': '/static/hero.css'}
        