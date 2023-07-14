from selenium import webdriver
from axe_selenium_python import Axe

def check_page_accessibility(url):
    # Inicializa e direciona o Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get(url)

    # Inicializa o objeto Axe para análise de acessibilidade
    axe = Axe(driver)
    axe.inject()

    # Executa a verificação de acessibilidade
    results = axe.run()

    # Exibe os problemas de acessibilidade
    if results["violations"]:
        print(f"{len(results['violations'])} problemas de acessibilidade encontrados na página:")
        for violation in results["violations"]:
            print(f"Message: {violation['help']}")
            print(f"Impact: {violation['impact']}")
            print("---")
    else:
        print("A página está de acordo com as diretrizes de acessibilidade WCAG.")

    driver.quit()

url = input("Digite o link da página a ser verificada: ")
check_page_accessibility(url)
