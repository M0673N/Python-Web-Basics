from django.shortcuts import render

from newDjangoProject.formsDemo.forms import DemoForm


def demo_form(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            print('VALIDATION SUCCESS')
            for key, value in form.cleaned_data.items():
                print(f'{key.upper()}: {value}')
        else:
            print(form.errors)
    else:
        return render(request, 'demo_form.html', context={'form': DemoForm()})
