APPARATI = []
STATI_AMMESSI = {"attivo", "in manutenzione", "guasto", "spento"}


def aggiungi_apparato(codice: str, stato: str) -> None:
    """Aggiunge un nuovo apparato al registro se codice e stato sono validi."""
    codice = codice.strip() if isinstance(codice, str) else ""

    if not codice:
        raise ValueError("Codice non valido")

    if any(apparato["codice"] == codice for apparato in APPARATI):
        raise ValueError("Codice duplicato")

    if stato not in STATI_AMMESSI:
        raise ValueError("Stato non ammesso")

    APPARATI.append({"codice": codice, "stato": stato})


def aggiorna_stato(codice: str, nuovo_stato: str) -> None:
    """Aggiorna lo stato di un apparato esistente."""
    codice = codice.strip() if isinstance(codice, str) else ""

    if not codice:
        raise ValueError("Codice non valido")

    if nuovo_stato not in STATI_AMMESSI:
        raise ValueError("Stato non ammesso")

    for apparato in APPARATI:
        if apparato["codice"] == codice:
            apparato["stato"] = nuovo_stato
            return

    raise ValueError("Codice non trovato")


__all__ = ["APPARATI", "aggiungi_apparato", "aggiorna_stato"]
