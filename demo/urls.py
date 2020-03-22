from demo import views

urlpatterns = [
    [r'/welcome/(?P<nickname>\w+)', views.welcome],
    [r'/foo', 'demo.urls2'],
]
