from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        ``collaborate_form``
            An instance of :form:`about.CollaborateForm`.

    **Template**
    :template:`about/about.html`
    """

    if request.method == "POST":
        print("Received a collaborator POST request")
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            print("Form validator:collaborator POST request")
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavor to respond within 2 working days."
            )

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    print("About to collab render template")
    

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form,
        },
    )