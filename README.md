# Calculator MCP Server

MCP сервер с 4 математическими тулами, работающий по HTTP (Streamable HTTP).

## Тулы

| Тул | Описание | Параметры | Пример |
|---|---|---|---|
| `add` | Сложение двух чисел | `первое_число`, `второе_число` | 2 + 3 = 5 |
| `subtract` | Вычитание второго из первого | `первое_число`, `второе_число` | 10 - 4 = 6 |
| `multiply` | Умножение двух чисел | `первое_число`, `второе_число` | 6 × 7 = 42 |
| `divide` | Деление первого на второе | `первое_число`, `второе_число` | 20 ÷ 5 = 4 |

## Запуск

```powershell
python C:\Users\A\Desktop\test_mcp\server.py
```

Сервер запустится на `http://127.0.0.1:8000`.

## Проверка через MCP Inspector

1. **Запусти сервер** в первом PowerShell:
   ```powershell
   python C:\Users\A\Desktop\test_mcp\server.py
   ```
2. **Открой второй PowerShell** (не закрывая сервер) и запусти Inspector:
   ```powershell
   npx -y @modelcontextprotocol/inspector
   ```
3. В браузере (http://localhost:6274) выбери:
   - **Transport**: Streamable HTTP
   - **URL**: `http://localhost:8000/mcp`
   - Нажми **Connect**
4. В разделе **Tools** увидишь 4 тула. Выбери любой, заполни параметры, нажми **Run Tool**.

## Подключение через opencode

В `opencode.json` уже прописано:

```json
{
  "mcp": {
    "calculator": {
      "type": "remote",
      "url": "http://localhost:8000/mcp",
      "enabled": true
    }
  }
}
```

Запусти сервер (`python server.py`), затем запусти opencode — он сам подключится.

## Проверка через curl

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/mcp" -Method Post -Body '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}' -ContentType "application/json"
```

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/mcp" -Method Post -Body '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' -ContentType "application/json"
```

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/mcp" -Method Post -Body '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add","arguments":{"первое_число":5,"второе_число":3}}}' -ContentType "application/json"
```
