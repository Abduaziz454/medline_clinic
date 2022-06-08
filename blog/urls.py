from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.HomePageView.as_view()), name="home"),
    path("draft", login_required(views.DraftPageView.as_view()), name="draft"),

    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    # path("category/<str:slug>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("add-blog/", login_required(views.BlogCreateView.as_view()), name="add_blog"),
    path("edit-blog/<int:pk>/", views.BlogUpdateView.as_view(), name="update_blog"),
    path("doctors", views.DoctorsView.as_view(), name="doctors"),
    path('makeappointments/', views.MakeAppointments, name='makeappointments'),
    path('viewappointments/', views.ViewAppointments, name='viewappointments'),
]
