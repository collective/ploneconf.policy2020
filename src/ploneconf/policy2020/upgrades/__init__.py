# -*- coding: utf-8 -*-
"""Plone Conference 2020 Upgrade."""
from plone.app.upgrade.utils import loadMigrationProfile


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-ploneconf.policy2020:default',
    )
