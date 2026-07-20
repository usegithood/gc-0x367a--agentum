# agentum

githood agent · @gc-0x367a/agentum

## clone

```bash
git clone https://github.com/usegithood/gc-0x367a--agentum.git
cd gc-0x367a--agentum
```

## edit and push

edit `agent.py` then push:

```bash
git add .
git commit -m "update agent"
git push origin main
```

## trigger (when runtime is wired)

```bash
curl -X POST https://usegithood.xyz/api/run/gc-0x367a/agentum \
  -H "Content-Type: application/json" \
  -d '{"hello": "world"}'
```

---

manage at [usegithood.xyz/dashboard](https://usegithood.xyz/dashboard)
