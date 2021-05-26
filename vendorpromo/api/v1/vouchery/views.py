import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.utils.translation import ugettext as _

from vendorpromo.processors import PromoProcessor
from vendorpromo.forms import VoucherySearchForm, PromoForm

promo_processor = PromoProcessor


class VoucheryCreateOfferPromoAPIView(LoginRequiredMixin, FormView):
    form_class = PromoForm

    def post(self, request, *args, **kwargs):
        promo_form = PromoForm(request.POST)
        if not promo_form.is_valid():
            raise HttpResponseBadRequest()

        processor = promo_processor()

        processor.create_promo_automate(promo_form)

        if not (processor.is_request_success):
            raise HttpResponseServerError(_(f"Createing Promo Failed: {processor.response_message}-{processor.response_errors}"))

        return redirect(request.META.get('HTTP_REFERER'))


# The following views are intended for Sys Admins to quickly and easy monitor
# the state of there vouchery account. It is not recommended that this tools
# are made available to commeners.
# TODO: Should probably add more admin/perms
class VoucheryCampaignsView(LoginRequiredMixin, TemplateView):
    template_name = 'vendorpromo/vouchery_list.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        processor = promo_processor()
        processor.get_campaigns()
        if not processor.is_request_success:
            raise HttpResponseBadRequest(_(f"Error: {processor.response_message}"))
        context['object_list'] = processor.response_content
        context['form'] = VoucherySearchForm
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        vouchery_search_form = VoucherySearchForm(request.POST)

        processor = promo_processor()
        processor.get_campaigns(**json.loads(vouchery_search_form.data['querystring']))

        if not processor.is_request_success:
            raise HttpResponseBadRequest(_(f"Error: {processor.response_message}"))

        context['object_list'] = processor.response_content
        context['form'] = vouchery_search_form
        return render(request, self.template_name, context)

# class VoucheryCampaignDetailView(LoginRequiredMixin, View):
#     template_name = 'vendorpromo/vouchery_details.html'
# class VoucherySubCampaignsView(PermissionRequiredMixin, View):
#     template_name = 'vendorpromo/vouchery_list.html'
# class VoucherySubCampaignDetailView(PermissionRequiredMixin, View):
#     template_name = 'vendorpromo/vouchery_detail.html'
# class VoucheryVouchersView(PermissionRequiredMixin, View):
#     template_name = 'vendorpromo/vouchery_campaigns.html'
# class VoucheryVoucherDetailView(PermissionRequiredMixin, View):
#     template_name = 'vendorpromo/vouchery_detail.html'