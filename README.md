# MINI_DIO

MINI_DIO is a research project for a small MCM-based artificial inner-field system.

The focus is not trading. Market data is currently used as a controlled external world because it provides time, movement, energy, rhythm and structural variance.

## Research Focus

MINI_DIO investigates whether a small MCM field can form:

- passive inner-field reactions,
- emergent meaning condensation,
- recurrent semantic islands,
- center/periphery topology,
- drift and transition phases,
- passive field self-regulation,
- cyclic field movement.

Current working hypothesis:

The MCM field appears to possess passive self-regulation. Center, bridge, drift and transition are not manually forced as action rules; they are read as emerging field roles.

## Related Research Directions

MINI_DIO is not built in isolation. There are related research directions and systems:

- **Active Inference / Free Energy Principle**  
  Models perception, action and self-organization through prediction, uncertainty and free-energy minimization.
- **Embodied AI and ecological perception**  
  Studies agents that perceive and act through situated sensorimotor coupling with an environment.
- **Neuromorphic and spiking-neural systems**  
  Build brain-inspired computation through neurons, spikes, temporal dynamics and energy-efficient processing.
- **Cognitive architectures such as OpenCog / OpenCog Hyperon**  
  Explore artificial cognition through multiple interacting knowledge and reasoning systems.
- **Neural simulators such as Nengo**  
  Provide tools for building large-scale neural and cognitive models.
- **Self-organizing and adaptive cognition research**  
  Studies how memory, structure and behavior can emerge from internal dynamics instead of fixed instruction chains.

MINI_DIO is close to these fields, but the MCM approach is different in its current focus:

- The central object is not prediction, reward, symbolic reasoning or trading performance, but **MCM-based inner-field reaction**.
- Sensory input is not used directly as action logic. It first becomes **field effect**: tension, carrying, strain, drift, recoupling and after-effect.
- Meaning is not assigned as a fixed label. It is read as **emergent meaning condensation** when similar inner-field states return.
- The system is currently passive. It observes whether field topology, semantic islands and self-regulation appear before any action layer is added.
- The key research question is whether a small artificial field can form reproducible inner order from world contact without hard-coded strategy logic.

In short: related systems often ask how an agent predicts, acts, reasons or optimizes. MINI_DIO currently asks how an MCM field internally reacts, organizes, condenses meaning and stabilizes itself before action.

## Project Layout

```text
mini_dio/      Core package: world, MCM neuron, field effects, memory, runner
reports/       Passive research reports and diagnostic scripts
docs/befunde/  Current research findings
data/          Local test worlds
memory/        Local MINI_DIO memory files
debug/         Local report and run outputs
tools/         Utility scripts
tests/         Future verification tests
```

## Important Boundary

MINI_DIO is currently passive research infrastructure.

Reports must not be interpreted as:

- trading rules,
- gates,
- entry signals,
- motor logic,
- proof of a universal MCM topology.

They are observations of passive field organization.

## Run

```powershell
python -m mini_dio.run_mini --data data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv
```

## Standard Research Chain

```powershell
python tools\run_research_chain.py
```

This runs two passive MINI_DIO passes on the same controlled world, compares both reports, and writes:

- `debug/research_chain/research_chain_summary.json`
- `docs/befunde/AKTUELLER_FORSCHUNGSLAUF.md`

If no data file is present, add a CSV with:

```text
timestamp_ms,open,high,low,close,volume
```

## Current Research Chain

The current documented findings are in `docs/befunde/107_...` through `120_...`.

The strongest current result is the passive MCM cycle map:

- center can hold,
- bridges carry center,
- drift can return to center,
- transition can recouple,
- drift/transition can pass through center into bridge states.

## Next Step

Evaluate passive cycle maturity:

- Which cycles are stable?
- Which cycles are open?
- Which cycles are strained?
- Which cycles are reorganizing?
