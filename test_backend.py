import unittest

from backend import processar_calculo_media, processar_simulacao


class BackendLogicTests(unittest.TestCase):
    def test_processar_calculo_media_retorna_media_e_status(self):
        resultado = processar_calculo_media({
            "av1": 8.0,
            "av2": 7.0,
            "av3": 9.0,
            "edag": 6.0,
        })

        self.assertAlmostEqual(resultado["media"], 7.65)
        self.assertEqual(resultado["status"], "aprovado")

    def test_processar_simulacao_retorna_nota_necessaria(self):
        resultado = processar_simulacao({"av1": 8.0, "av2": 7.0})

        self.assertEqual(resultado["tipo"], "simulacao")
        self.assertAlmostEqual(resultado["nota_atual"], 3.75)
        self.assertAlmostEqual(resultado["nota_necessaria"], 6.5)

    def test_processar_simulacao_completo_retorna_media(self):
        resultado = processar_simulacao({
            "av1": 5.0,
            "av2": 5.0,
            "av3": 5.0,
            "edag": 5.0,
        })

        self.assertEqual(resultado["tipo"], "completo")
        self.assertAlmostEqual(resultado["media"], 5.0)
        self.assertEqual(resultado["status"], "reprovado")


if __name__ == "__main__":
    unittest.main()
