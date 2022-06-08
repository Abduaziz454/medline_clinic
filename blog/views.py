from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib import messages
from .models import Blog, Category
from .forms import BlogForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from auth_app.models import Users, Appointment
from django.utils import timezone


class HomePageView(ListView):
    template_name = "home.html"
    context_object_name = "blogs"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     context["categories"] = Category.objects.all()
    #     context["users"] = Users.objects.all()
    #     return context


class DraftPageView(ListView):
    template_name = "draft.html"
    context_object_name = "blogs"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Blog.objects.filter(is_published=False)


def blog_detail(request, pk=None):
    blog = Blog.objects.get(pk=pk)
    categories = Category.objects.all()
    return render(request, "blog_detail.html", context={
        "blog": blog,
        "categories": categories,
    })


class CategoryDetailView(DetailView):
    context_object_name = "category"
    template_name = "home.html"

    def get_queryset(self):
        return Category.objects.filter(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context["blog"] = Blog.objects.filter(category__slug=self.kwargs["slug"], is_published=True)
        context["title"] = self.get_object().name
        context["categories"] = Category.objects.all()
        return context


class BlogCreateView(CreateView):
    template_name = "update_blog.html"
    form_class = BlogForm
    extra_context = {
        "btn_text": "Create",
        "btn_color": "success",
    }

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)

    def get_success_url(self):
        blog = self.object
        messages.success(self.request, f"Success")
        return self.object.get_absolute_url()


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "update_blog.html"
    form_class = BlogForm
    extra_context = {
        "btn_text": "Update",
        "btn_color": "success",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        return context

    def get_success_url(self):
        blog = self.object
        return self.object.get_absolute_url()


class DoctorsView(ListView):
    template_name = "doctors.html"
    context_object_name = "doctors"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Users.objects.filter(user_type="Doctor")


def MakeAppointments(request):
    alldoctors = Users.objects.filter(user_type="Doctor")
    d = {'alldoctors': alldoctors}

    if request.method == 'POST':
        doctoremail = request.POST['doctoremail']
        doctorname = request.POST['doctorname']
        patientname = request.POST['patientname']
        patientemail = request.POST['patientemail']
        appointmentdate = request.POST['appointmentdate']
        appointmenttime = request.POST['appointmenttime']
        symptoms = request.POST['symptoms']
        try:
            Appointment.objects.create(doctorname=doctorname, doctoremail=doctoremail, patientname=patientname,
                                       patientemail=patientemail, appointmentdate=appointmentdate,
                                       appointmenttime=appointmenttime, symptoms=symptoms, status=True, prescription="")
            error = "no"
        except:
            error = "yes"
        e = {"error": error}
        return render(request, 'appointment.html', e)
    elif request.method == 'GET':
        return render(request, 'appointment.html', d)


def ViewAppointments(request):
    upcomming_appointments = Appointment.objects.filter().order_by('appointmentdate')
    d = {"upcomming_appointments": upcomming_appointments}
    return render(request, 'view_appoint.html', d)
