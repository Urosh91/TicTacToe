from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login, authenticate

from .forms import InvitationForm, RegisterForm
from .models import Invitation
from gameplay.models import Game


@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    finished_games = my_games.difference(active_games)
    invitations = request.user.invitations_received.all()
    return render(request, "player/home.html", {"active_games": active_games, "finished_games": finished_games,
                                                "invitations": invitations})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("player_home")
    else:
        form = RegisterForm()
    return render(request, "player/user_registration_form.html", {"form": form})


@login_required
def new_invitation(request):
    if request.method == "POST":
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("player_home")
    else:
        form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {"form": form})


@login_required
def accept_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == "POST":
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user,
            )
        invitation.delete()
        return redirect(game)
    else:
        return render(request, "player/accept_invitation_form.html", {"invitation": invitation})
