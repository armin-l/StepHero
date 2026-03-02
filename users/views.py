from django.shortcuts import render, get_object_or_404
from .models import Group

def group_statistics(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    total_steps = sum(user.steps for user in group.members.all())
    average_steps = total_steps / group.members.count() if group.members.count() > 0 else 0

    context = {
        'group': group,
        'total_steps': total_steps,
        'average_steps': average_steps,
        'member_count': group.members.count(),
    }
    return render(request, 'group_statistics.html', context)

def leaderboard(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    members = group.members.all().order_by('-steps')

    context = {
        'group': group,
        'members': members,
    }
    return render(request, 'leaderboard.html', context)