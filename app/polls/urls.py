from django.urls import path, include

from .views import cbv, fbv as views


app_name = 'polls'

urlpatterns_cbv = [
    path('', cbv.IndexView.as_view(), name='index')
]

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('cbv/', include(urlpatterns_cbv))
]