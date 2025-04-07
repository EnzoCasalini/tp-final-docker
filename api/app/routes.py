from fastapi import APIRouter, Form
from db import get_connection

router = APIRouter()


@router.get("/user/adresses")
def get_adresses():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM adresse")
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result


@router.post("/admin/adresses")
def create_adresse(
    numero_rue: str = Form(...),
    nom_rue: str = Form(...),
    ville: str = Form(...),
    code_postal: str = Form(...)
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO adresse (numero_rue, nom_rue, ville, code_postal)
        VALUES (%s, %s, %s, %s)
    """, (numero_rue, nom_rue, ville, code_postal))

    conn.commit()
    cursor.close()
    conn.close()

    return {
        "message": "Adresse ajoutée avec succès",
        "data": {
            "numero_rue": numero_rue,
            "nom_rue": nom_rue,
            "ville": ville,
            "code_postal": code_postal
        }
    }