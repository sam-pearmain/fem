import jax

def main():
    print(jax.device_count(), jax.devices())

if __name__ =="__main__":
    main()