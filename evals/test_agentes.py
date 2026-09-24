"""
Evals offline do sistema multiagente.

Não chamam a API da OpenAI — rodam no CI sem chave e sem custo. Conferem o
que dá para conferir sem o modelo: ferramentas funcionam, e cada perfil de
agente (agent*.md) tem a estrutura que o template exige.

Rode com:  python -m unittest discover -s evals -v
"""

import json
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

import agent  # noqa: E402

PERFIS = sorted(RAIZ.glob("agent*.md"))
SECOES_OBRIGATORIAS = ["## Identidade", "## Como você responde", "## Regras", "## Ferramentas disponíveis"]


class TestFerramentas(unittest.TestCase):
    def test_somar_e_exata(self):
        self.assertEqual(json.loads(agent.executar_ferramenta("somar", {"a": 1234, "b": 5678})), {"resultado": 6912})

    def test_ferramenta_inexistente_vira_erro_e_nao_crash(self):
        self.assertIn("erro", json.loads(agent.executar_ferramenta("nao_existe", {})))

    def test_argumento_errado_vira_erro_e_nao_crash(self):
        self.assertIn("erro", json.loads(agent.executar_ferramenta("somar", {"a": 1})))

    def test_toda_ferramenta_declarada_tem_executor(self):
        for ferramenta in agent.FERRAMENTAS:
            with self.subTest(ferramenta=ferramenta["function"]["name"]):
                self.assertIn(ferramenta["function"]["name"], agent.EXECUTORES)

    def test_toda_ferramenta_tem_descricao_util(self):
        # Descrição vaga = ferramenta ignorada pelo modelo (ver README).
        for ferramenta in agent.FERRAMENTAS:
            with self.subTest(ferramenta=ferramenta["function"]["name"]):
                self.assertGreaterEqual(len(ferramenta["function"].get("description", "")), 20)


class TestPerfisDeAgente(unittest.TestCase):
    def test_existe_pelo_menos_um_perfil(self):
        self.assertTrue(PERFIS)

    def test_perfis_tem_secoes_obrigatorias(self):
        for perfil in PERFIS:
            texto = perfil.read_text(encoding="utf-8")
            for secao in SECOES_OBRIGATORIAS:
                with self.subTest(perfil=perfil.name, secao=secao):
                    self.assertIn(secao, texto)

    def test_perfis_documentam_todas_as_ferramentas(self):
        for perfil in PERFIS:
            texto = perfil.read_text(encoding="utf-8")
            for nome in agent.EXECUTORES:
                with self.subTest(perfil=perfil.name, ferramenta=nome):
                    self.assertIn(f"`{nome}`", texto)

    def test_contexto_inclui_memoria(self):
        self.assertIn("# Memória", agent.carregar_contexto())


if __name__ == "__main__":
    unittest.main()
