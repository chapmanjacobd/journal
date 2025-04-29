print(f"{' [ Run Status ] ':=^50}")
print(f"[{time:%H:%M:%S}] Training Run {run_id=} status: {progress:.1%}")
print(f"Summary: {total_samples:,} samples processed")
print(f"Accuracy: {accuracy:.4f} | Loss: {loss:#.3g}")
print(f"Memory: {memory / 1e9:+.2f} GB")

print(f"{name=}, {age=}")

print(f"Number: {num:09}")

print(f"Left: |{word:<10}|")
print(f"Right: |{word:>10}|")
print(f"Center: |{word:^10}|")
print(f"Center *: |{word:*^10}|")

print(f"Date: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")

