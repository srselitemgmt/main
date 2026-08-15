# Reminder: Set up the Plaud MCP connection

**Created:** 2026-08-15
**Status:** Open
**Calendar reminder:** Mon 2026-08-17, 8:30–8:45 AM MT (popup + email at event time)
**Docs:** https://docs.plaud.ai/plaud-mcp-cli/mcp

## To do

Connect the Plaud recorder to the AI assistant so recordings, transcripts, and
action items are searchable alongside the existing meeting tools.

### Recommended: Claude Web connector (no terminal required)

1. Go to claude.ai, open the left sidebar, click **Customize > Connectors**.
2. Search for **Plaud Web MCP** and click Connect.
3. Sign in to Plaud and click **Authorize**.

This is the same mechanism as the Fireflies, Zoom, Gmail, Calendar, and Slack
connectors already in use, so it is expected to be available in remote Claude
Code sessions as well — unverified until connected.

**Privacy tradeoff:** over the web connector, recording data passes through
Plaud's US-hosted MCP server. Per Plaud's docs it is processed in transit and
not stored after the request completes. For sensitive client or deal
conversations, prefer the local install below, which keeps traffic local.

### Alternative: local install

```
npx -y @plaud-ai/mcp@latest install
```

- Requires Node.js >= 20 and a Plaud account.
- Auto-detects Claude Code, Claude Desktop, Codex Desktop, Cursor/Windsurf/
  VS Code/Zed, and Kiro.
- After install, **fully exit and start a new `claude` session** — reopening the
  window is not enough.
- Then ask the client: "log me into Plaud".
- `--no-login` skips browser sign-in on headless machines; `--yes` configures all
  detected clients without prompts.

Package verified against the npm registry: `@plaud-ai/mcp`, published by
`plaud-dev` (harold.guo@plaud.ai), latest `0.3.8` as of 2026-08-10.

## What it unlocks

**Tools:** `login`, `logout`, `get_current_user`, `list_files`, `get_file`,
`get_note`, `get_transcript`.

- `list_files` filters on `query` (keyword match on recording name), `date_from`,
  and `date_to` (both `YYYY-MM-DD`).
- `get_transcript` returns the full transcript with timestamps and speaker labels.
- `get_note` returns the AI summary, action items, and key topics.
- `get_file` adds a 24-hour presigned audio URL, transcript segments, and
  Markdown notes.

**Skills** (auto-load on install): `plaud-browse`, `plaud-find`, `plaud-read`,
`plaud-digest` ("what meetings did I have this week"), `plaud-followup`
("draft a follow-up email", "list the action items"), `plaud-export`
("save to Notion", "post to Slack").

## Why this matters

Fireflies, Otter, Read.ai, Fathom, and Zoom AI already cover Zoom calls, but
none capture in-person conversations. Plaud is the only source covering pod
meetings, meetups, and face-to-face conversations — including any in-person
follow-up with Rich on the Owners Club sponsorship items.

## Note on this environment

The Plaud domains (`plaud.ai`, `api.plaud.ai`, `docs.plaud.ai`) are blocked by
the remote container's egress proxy, and the container is ephemeral, so the
local install cannot be performed from a Claude Code web session. The web
connector path avoids this entirely since it runs server-side.
