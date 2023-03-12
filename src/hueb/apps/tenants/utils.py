from .models import Tenant


def hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(":")[0].lower().split(".")[0]


def tenant_from_request(request):
    hostname = hostname_from_request(request)
    subdomain_prefix = hostname
    if Tenant.objects.filter(subdomain_prefix=subdomain_prefix).exists():
        return Tenant.objects.filter(subdomain_prefix=subdomain_prefix).first()
    else:
        return None


def tenantname_from_request(request):
    tenant = tenant_from_request(request)
    return tenant.name if tenant else None
