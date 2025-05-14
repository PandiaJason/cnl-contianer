
# 🧰 Network Tools - Basic Commands

This experiment introduces essential network diagnostic tools. Use these tools inside the Docker container to analyze connectivity, DNS resolution, interface configuration, and traffic.

---

## 1️⃣ `ping`

Tests connectivity to another host.

```bash
ping google.com
```

---

## 2️⃣ `traceroute`

Shows the path packets take to reach a host.

```bash
traceroute google.com
```

---

## 3️⃣ `nslookup`

Resolves a domain name to its IP address.

```bash
nslookup google.com
```

---

## 4️⃣ `netstat`

Displays network connections, routing tables, and interface stats.

```bash
netstat -tulnp
```

---

## 5️⃣ `tcpdump`

Captures network packets.

```bash
tcpdump -i eth0
```

Example: To capture ICMP (ping) packets:

```bash
tcpdump icmp
```

---

## 6️⃣ `ifconfig` / `ip a`

Displays IP configuration of interfaces.

```bash
ifconfig
```

Or

```bash
ip a
```

---

🧪 Try exploring these tools with different flags and targets!
