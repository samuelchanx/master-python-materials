# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adsinsights import AdsInsights
from facebookads.api import FacebookAdsApi

access_token = 'EAAYG2ZAH8iM0BAD5JMVSQrO7wDGZBHE0WA4VbgfWHX93plZCARrZBQxyyhSkC8Eu6JNhkzgwU5f99wseuLzjSnVxkP74ZAEPNLAFAXkmX1LdeRxzvPqcyJbG5jUjLcLjGoz77Mjmsu22xAr2ZAwtcigScglYbk1yllWQhjadNd8oZAaV2g055EJZAeUWMCMrjIoZD'
ad_account_id = 'act_250617589348447'
app_secret = '2e8c4e640bd999f94838ab90d904fa79'
app_id = '1696381387180237'
FacebookAdsApi.init(access_token=access_token)

fields = [
    'results',
    'result_rate',
    'reach',
    'frequency',
    'impressions',
    'delivery',
    'spend',
    'impressions_gross',
    'impressions_auto_refresh',
    'quality_score_organic',
    'quality_score_ectr',
    'quality_score_ecvr',
    'cost_per_result',
    'cpp',
    'cpm',
    'actions:page_engagement',
    'actions:like',
    'actions:comment',
    'actions:post_engagement',
    'actions:post_reaction',
    'actions:onsite_conversion_post_save',
    'actions:post',
    'actions:photo_view',
    'actions:rsvp',
    'actions:checkin',
    'actions:full_view',
    'unique_actions:full_view',
    'ar_effect_share:ar_effect_share',
    'cost_per_action_type:page_engagement',
    'cost_per_action_type:like',
    'cost_per_action_type:post_engagement',
    'cost_per_action_type:rsvp',
    'unique_video_continuous_2_sec_watched_actions:video_view',
    'video_continuous_2_sec_watched_actions:video_view',
    'actions:video_view',
    'video_thruplay_watched_actions:video_view',
    'video_p25_watched_actions:video_view',
    'video_p50_watched_actions:video_view',
    'video_p75_watched_actions:video_view',
    'video_p95_watched_actions:video_view',
    'video_p100_watched_actions:video_view',
    'video_avg_time_watched_actions:video_view',
    'video_play_actions:video_view',
    'canvas_avg_view_time',
    'canvas_avg_view_percent',
    'cost_per_2_sec_continuous_video_view:video_view',
    'cost_per_action_type:video_view',
    'cost_per_thruplay:video_view',
    'actions:link_click',
    'unique_actions:link_click',
    'outbound_clicks:outbound_click',
    'unique_outbound_clicks:outbound_click',
    'website_ctr:link_click',
    'unique_link_clicks_ctr',
    'outbound_clicks_ctr:outbound_click',
    'unique_outbound_clicks_ctr:outbound_click',
    'clicks',
    'unique_clicks',
    'ctr',
    'unique_ctr',
    'cost_per_action_type:link_click',
    'cost_per_unique_action_type:link_click',
    'cost_per_outbound_click:outbound_click',
    'cost_per_unique_outbound_click:outbound_click',
    'cpc',
    'cost_per_unique_click',
    'estimated_ad_recallers',
    'estimated_ad_recall_rate',
    'cost_per_estimated_ad_recallers',
]
params = {
    'level': 'adset',
    'filtering': [],
    'breakdowns': [],
    'time_range': {'since':'2020-04-21','until':'2020-05-21'},
}
print(AdAccount(ad_account_id).get_insights(
    fields=fields,
    params=params,
)) 