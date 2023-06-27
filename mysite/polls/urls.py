from django.urls import path

from . import views



app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("recent", views.RecentPollsView.as_view(), name="recent"),
    path("list", views.PollsListView.as_view(), name="polls"),
    path("daily", views.DailyPollView.as_view(), name="daily"),
    path("random", views.RandomPollView.as_view(), name="random"),
    path("popular", views.PopularPollsView.as_view(), name="popular"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
] 