from app.models.supabase_client import supabase

PRODUCTS_TABLE = "produtos"

def get_all_products():
    """"Recupera todo sprodutos"""

    try:
        response = supabase.table(PRODUCTS_TABLE).select("*").execute()
        if response.error:
            print(f"erro {response.error.message}")
            return[]
        return response.data
    except Exception as e:
        print({e})