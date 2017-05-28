from mvm_server.mvm_server_app.models import CaseHuile, Minion

def areCaseHuile(pminion, pmove):
    is_case_huile = False
    cases_huiles = CaseHuile.objects.all()
    for case_huile in cases_huiles:
        if case_huile.posX == pminion.posX and case_huile.posY == pminion.posY:
            is_case_huile = True

    if is_case_huile:
        move(pminion, pmove)

def areMinion(pSelectedMinion):
    moveOK = True
    for minion in Minion.objects.all():
        if minion.posX == pSelectedMinion.posX and minion.posY == pSelectedMinion.posY:
            moveOK = False

    return moveOK


moveFunctions = {
        100: lambda posX, posY: (posX + 1, posY),
        113: lambda posX, posY: (posX - 1, posY),
        122: lambda posX, posY: (posX, posY - 1),
        115: lambda posX, posY: (posX, posY + 1),
}

def move(pSelectedMinion, pmove):

    moveFunction = moveFunctions[int(pmove)]
    pSelectedMinion.posX, pSelectedMinion.posY = moveFunction(pSelectedMinion.posX,
                                                              pSelectedMinion.posY)
    if areMinion(pSelectedMinion):
        pSelectedMinion.save()
        areCaseHuile(pSelectedMinion, pmove)
    else:
        pSelectedMinion.refresh_from_db()

