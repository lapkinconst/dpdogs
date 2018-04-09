from django.conf.urls import url
from authenticate.views import RegisterFormView, LoginFormView, LogoutView, upload_file


urlpatterns = [
    url(r'^signup/$', RegisterFormView.as_view(), name="sign_up"),
    url(r'^login/$', LoginFormView.as_view(), name="log_in"),
    url(r'^logout/$', LogoutView.as_view(), name="log_out"),
    url(r'^profile/$', upload_file, name="profile")
]