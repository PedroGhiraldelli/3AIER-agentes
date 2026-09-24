## O que muda

<!-- Uma ou duas frases: o que este PR faz e por quê. -->

## Qual agente / parte do sistema

- [ ] Núcleo (`agent.py` — loop, ferramentas)
- [ ] Interface (`app.py`)
- [ ] Prompt de sistema (`agent*.md`)
- [ ] Memória (`memory.md`)
- [ ] Evals / CI

---

## Checklist obrigatório

### Testou o agente?
- [ ] Rodei o agente localmente (`python agent.py` ou `streamlit run app.py`)
- [ ] Testei o caso que motivou a mudança
- [ ] Testei pelo menos um caso que **não deveria** mudar de comportamento

**Como testei** (cole a pergunta e um trecho da resposta):

```
você> 
agente> 
```

### Rodou os evals?
- [ ] Rodei `python -m unittest discover -s evals -v` e todos passaram
- [ ] Se criei ferramenta ou perfil de agente novo, adicionei eval para ele

### Documentou o prompt alterado?
- [ ] Não alterei nenhum prompt (`agent*.md` / `memory.md`) — pule esta seção
- [ ] Alterei prompt e descrevo abaixo **o que** mudou e **qual comportamento** espero

**Prompt alterado:**

| Arquivo | Antes | Depois | Comportamento esperado |
|---|---|---|---|
|  |  |  |  |

### Segurança
- [ ] Não commitei `.env` nem nenhuma chave de API
