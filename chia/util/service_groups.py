from __future__ import annotations

from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "platinum_harvester",
        "platinum_timelord_launcher",
        "platinum_timelord",
        "platinum_farmer",
        "platinum_full_node",
        "platinum_wallet",
        "platinum_data_layer",
        "platinum_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["platinum_wallet", "platinum_data_layer"],
    "data_layer_http": ["platinum_data_layer_http"],
    "node": ["platinum_full_node"],
    "harvester": ["platinum_harvester"],
    "farmer": ["platinum_harvester", "platinum_farmer", "platinum_full_node", "platinum_wallet"],
    "farmer-no-wallet": ["platinum_harvester", "platinum_farmer", "platinum_full_node"],
    "farmer-only": ["platinum_farmer"],
    "timelord": ["platinum_timelord_launcher", "platinum_timelord", "platinum_full_node"],
    "timelord-only": ["platinum_timelord"],
    "timelord-launcher-only": ["platinum_timelord_launcher"],
    "wallet": ["platinum_wallet"],
    "introducer": ["platinum_introducer"],
    "simulator": ["platinum_full_node_simulator"],
    "crawler": ["platinum_crawler"],
    "seeder": ["platinum_crawler", "platinum_seeder"],
    "seeder-only": ["platinum_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
