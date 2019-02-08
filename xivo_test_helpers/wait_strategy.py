# -*- coding: utf-8 -*-
# Copyright 2016-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


class WaitStrategy(object):

    def wait(self, integration_test):
        raise NotImplementedError()


class NoWaitStrategy(WaitStrategy):

    def wait(self, integration_test):
        pass
