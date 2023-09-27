from django.shortcuts import render
from django.views import generic

from products.models import Category


class HomePageView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AboutUsPageView(generic.TemplateView):
    template_name = 'pages/aboutus.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AboutUsPageView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ContactUsView(generic.TemplateView):
    template_name = 'pages/contactus.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ContactUsView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
