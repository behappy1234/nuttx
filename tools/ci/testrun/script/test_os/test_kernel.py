#!/usr/bin/env python3
# encoding: utf-8
import pytest

pytestmark = [pytest.mark.kerneltest]
cmocka_list_start = "cmocka_list_start"
cmocka_list_end = "cmocka_list_end"


@pytest.mark.run(order=-1)
def test_kernel(p):
    p.sendCommand(f"echo {cmocka_list_start}")
    ret = p.sendCommand("cmocka", "Cmocka Test Completed", timeout=300)
    p.sendCommand(f"echo {cmocka_list_end}")
    assert ret == 0
    print(f"debug ret={ret}")
