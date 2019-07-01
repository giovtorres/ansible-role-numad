import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', ['numad', 'numactl'])
def test_numad_package(host, pkg):
    assert host.package(pkg).is_installed


def test_numad_config(host):
    f = host.file("/etc/numad.conf")
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


def test_numad_service(host):
    s = host.service('numad')
    assert s.is_enabled
    assert s.is_running
