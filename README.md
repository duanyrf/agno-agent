# Pip — agente pessoal com Agno e AgentOS

Projeto introdutório baseado no tutorial oficial [Build a personal agent](https://docs.agno.com/first-agent). O agente mantém projetos, tarefas, decisões e notas usando as ferramentas `FileSystem` do Agno. Os dados e o histórico ficam em SQLite. O servidor é oferecido pelo AgentOS.

O modelo configurado é o roteador gratuito `openrouter/free`. O OpenRouter não cobra por tokens desse roteador, mas pode aplicar limites de uso e disponibilidade. É necessário ter uma conta e uma chave de API; não é necessário adicionar créditos para usar o modelo gratuito. O roteador pode escolher modelos diferentes entre chamadas.

## Requisitos

- Python 3.14
- [uv](https://docs.astral.sh/uv/)
- Chave de API do [OpenRouter](https://openrouter.ai/)

## Configurar e executar

Na pasta `agno-agent`, copie o arquivo de exemplo para `.env` e substitua o valor pela sua chave:

```bash
cp .env.example .env
```

No PowerShell:

```powershell
Copy-Item .env.example .env
```

Instale as dependências e inicie o AgentOS:

```bash
uv sync
uv run python personal_agent.py
```

O AgentOS ficará disponível em `http://localhost:7777`; a documentação interativa da API fica em `http://localhost:7777/docs`. Para conversar pela interface do Agno, conecte o AgentOS local no Control Plane conforme o [tutorial oficial](https://docs.agno.com/first-agent).

O banco SQLite será criado em `data/personal_agent.db`. A pasta `data/` está no `.gitignore` porque contém dados locais do agente.

## Exemplo de conversa

Experimente enviar ao Pip:

> Estou atualizando o guia de integração de novos clientes. Salve esse projeto e as próximas tarefas: enviar o rascunho para Jen na quinta-feira e testar as etapas com uma pessoa nova na sexta-feira.

Depois, em outra conversa, pergunte:

> Em que ponto está o guia de integração e qual é o próximo passo?

O agente consulta as notas salvas no seu espaço de arquivos para responder. O identificador `user_id` recebido pelo AgentOS define o namespace dos arquivos.

## Arquivos principais

- `personal_agent.py`: agente, armazenamento e servidor AgentOS.
- `.env.example`: modelo da variável necessária para OpenRouter.
- `pyproject.toml` e `uv.lock`: dependências e versões resolvidas pelo `uv`.
