from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://stevemorse.org/dl/dl.html")

    # Aguarda o carregamento da página
    page.wait_for_selector('xpath=/html/body/center/form/select[1]')

    lastname = "Borges"
    firstname = "Marcelo"
    middlename = "Souza"
    dobmonth = "August"
    dobday = "1"
    dobyear = "76"

    # Seleciona os capos e preencher

    # Campos de preenchimento
    page.fill('xpath=/html/body/center/form/input[1]', lastname)
    page.fill('xpath=/html/body/center/form/input[2]', firstname)
    page.fill('xpath=/html/body/center/form/input[3]', middlename)
    # Campos de seletor
    page.select_option('xpath=/html/body/center/form/select[2]', label=dobmonth)
    page.select_option('xpath=/html/body/center/form/span[1]/select', label=dobday)
    page.select_option('xpath=/html/body/center/form/span[2]/select', label=dobyear)

    # Esperar para criar o Licence number
    expect(page.locator("xpath=/html/body/center/form/font/span")).not_to_have_text("")

    # capturar o LN gerado
    license_number = page.locator("xpath=/html/body/center/form/font/span").inner_text()
    print(f"License number capturado: {license_number}")

    print("Pressione Enter para sair...")
    input()

    browser.close()

