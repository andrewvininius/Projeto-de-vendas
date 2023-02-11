cabecalho = ["Lojas"] + [store.store for store in stores] + ["Subtotal"]
linhas= [([product.product] + [None for store in stores] + [(0,0,0,None,product.product)])
            for product in products
        ]+

[["Subtotal"] + [(0,0,0,store.store,None) for store in stores] + [(0,0,0,None,None)]]

def soma_tuplas(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2], a[3], a[4])

for pev in Quotation.objects.all():
    total = pev.price * pev.quantity

    i0 = index_product[pev.product_id]
    i1 = index_store[pev.store_id] + 1
    valor = (pev.price, pev.quantity, total, pev.store, pev.product)

    linhas[i0][i1] = valor

    # Subtotal da linha (se fizer sentido no seu caso)
    linhas[i0][len(stores)+1] = soma_tuplas(linhas[i0][len(stores)+1], valor)

    # Subtotal da coluna (se fizer sentido no seu caso)
    linhas[len(produtos)][i1] = soma_tuplas(linhas[len(produtos)][i1], valor)

    # Total da tabela (se fizer sentido no seu caso)
    linhas[len(produtos)][len(stores)+1] = soma_tuplas(linhas[len(produtos)][len(stores)+1], valor)
