<script>
  import { onMount } from 'svelte';
  let reminders;

  onMount(async () => {
    await fetch(`http://127.0.0.1:8000/get-reminders/`)
      .then((r) => r.json())
      .then((data) => {
        reminders = data;
      });
  });
</script>

<main>
  <h1>Daily Reminders</h1>

  {#if reminders}
    {#each reminders as reminder}
      <ul>
        <li>{reminder}</li>
      </ul>
    {/each}
  {:else}
    <p class="loading">loading...</p>
  {/if}
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
