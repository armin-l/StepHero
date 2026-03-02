from django.shortcuts import redirect
from django.http import JsonResponse
from google_auth_oauthlib.flow import Flow
import os

GOOGLE_FIT_SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read']

flow = Flow.from_client_secrets_file(
    os.path.join(os.path.dirname(__file__), '../client_secret.json'),
    scopes=GOOGLE_FIT_SCOPES,
    redirect_uri='http://localhost:8000/google-fit/callback'
)

def google_fit_connect(request):
    authorization_url, state = flow.authorization_url()
    request.session['google_fit_state'] = state
    return redirect(authorization_url)

def google_fit_callback(request):
    flow.fetch_token(authorization_response=request.get_full_path())
    credentials = flow.credentials
    return JsonResponse({
        'access_token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_expiry': credentials.expiry.isoformat(),
    })