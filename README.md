# 🧪 Urban Routes - CI/CD con Selenium y GitHub Actions

Este proyecto demuestra la automatización de pruebas **Selenium WebDriver** integrada con **GitHub Actions (CI/CD)**.  
Forma parte de mi práctica profesional como **QA Engineer**, validando la ejecución automática de tests en un entorno continuo.

---

## 🚀 Tecnologías utilizadas
- **Python 3.10**
- **Selenium WebDriver**
- **Pytest**
- **WebDriver Manager**
- **GitHub Actions (CI/CD)**

---

## 🧩 Estructura del proyecto

urban-routes-ci-cd/
├── .github/
│ └── workflows/
│ └── selenium-tests.yml
├── tests/
│ └── test_main.py
├── requirements.txt
└── README.md

---

## ⚙️ Cómo funciona el pipeline

Cada vez que se realiza un **push** o **pull request** en la rama `main`, GitHub Actions ejecuta automáticamente:

1. Configuración de entorno Python en Ubuntu.
2. Instalación de dependencias (Selenium, Pytest, WebDriver Manager).
3. Ejecución de los tests definidos en `tests/test_main.py`.

---

## ✅ Ejemplo de prueba (`test_main.py`)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_open_python_org():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.python.org")
    assert "Python" in driver.title
    driver.quit()
```
Esta prueba abre la web de python.org
 y valida que el título contenga la palabra “Python”.
 
## 🧱 Flujo de integración continua (CI/CD)

El flujo está definido en .github/workflows/selenium-tests.yml
y contiene estos pasos principales:

- Checkout repository  
- Set up Python  
- Install dependencies  
- Run Selenium tests

## 🧑‍💻 Autor

Benjamín Vera
QA Engineer | Automatización de pruebas | CI/CD con GitHub Actions
📫 LinkedIn
www.linkedin.com/in/benjamin-vera-qa

📂 GitHub
https://github.com/Benjamin-vera-QA
