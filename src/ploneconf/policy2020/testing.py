# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf.policy2020


class PloneconfPolicy2020Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ploneconf.policy2020)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneconf.policy2020:default')


PLONECONF_POLICY2020_FIXTURE = PloneconfPolicy2020Layer()


PLONECONF_POLICY2020_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONECONF_POLICY2020_FIXTURE,),
    name='PloneconfPolicy2020Layer:IntegrationTesting',
)


PLONECONF_POLICY2020_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONECONF_POLICY2020_FIXTURE,),
    name='PloneconfPolicy2020Layer:FunctionalTesting',
)


PLONECONF_POLICY2020_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONECONF_POLICY2020_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PloneconfPolicy2020Layer:AcceptanceTesting',
)
