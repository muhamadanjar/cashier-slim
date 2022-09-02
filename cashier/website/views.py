from django.shortcuts import render
from django.views import View


class WebsiteIndexView(View):
    template_name = "website/index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)