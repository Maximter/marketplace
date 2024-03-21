from django.contrib.auth.decorators import user_passes_test

# Check if user belongs to group
def group_required(group_name):
    def in_group(u):
        if u.is_authenticated:
            if u.groups.filter(name=group_name).exists() or u.is_superuser:
                return True
        return False
    return user_passes_test(in_group)
