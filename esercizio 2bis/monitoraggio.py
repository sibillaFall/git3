SOGLIA_ORE = 100

aeromobili = [
    {
        "matricola": "I-ABCD",
        "modello": "Cessna 172",
        "ore_volo": 85,
        "controlli_ok": True,
    },
    {
        "matricola": "I-EFGH",
        "modello": "Piper PA-28",
        "ore_volo": 120,
        "controlli_ok": False,
    },
    {
        "matricola": "I-IJKL",
        "modello": "Diamond DA40",
        "ore_volo": 65,
        "controlli_ok": True,
    },
    {
        "matricola": "I-MNOP",
        "modello": "Cessna 182",
        "ore_volo": 105,
        "controlli_ok": False,
    },
]


def filtra_controlli_non_ok(aeromobili):
    return [aeromobile for aeromobile in aeromobili if aeromobile["controlli_ok"] == False]


def filtra_oltre_soglia(aeromobili, soglia_ore):
    return [aeromobile for aeromobile in aeromobili if aeromobile["ore_volo"] > soglia_ore]


def stampa_riepilogo(aeromobili):
    print(f"Riepilogo aeromobili: {len(aeromobili)}")
    for aeromobile in aeromobili:
        stato = (
            "manutenzione necessaria"
            if aeromobile["ore_volo"] >= SOGLIA_ORE
            else "regolare"
        )
        print(
            f"{aeromobile['matricola']} - {aeromobile['modello']}: "
            f"{aeromobile['ore_volo']} ore di volo ({stato})"
        )