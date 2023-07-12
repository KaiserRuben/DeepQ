<template>
  <ion-app>
    <ion-router-outlet/>
  </ion-app>
</template>

<script setup lang="ts">
import {IonApp, IonRouterOutlet} from '@ionic/vue';
</script>

<style>
a {
  text-decoration: none;
  color: var(--ion-color-secondary) !important;
}

a:hover {
  text-decoration: underline;
}

.router-link-active {
  color: var(--ion-color-primary) !important;
}

.router-link-active:hover {
  text-decoration: none;
}
</style>