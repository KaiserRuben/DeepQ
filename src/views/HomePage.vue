<template>
  <ion-page>
    <ion-content :fullscreen="true" :scroll-y="false">
      <div class="content" @click="nextQuestion">

        <div :class="showHelper?'helper':'hidden'">
          <span v-if="lang==='de'">
            Klicke auf den Bildschirm, um die nächste Frage zu sehen.
          </span>
          <span v-else>
            Click on the screen to see the next question.
          </span>
        </div>

        <div>
          <router-link to="/de" class="active">DE</router-link>
          |
          <router-link to="/en">EN</router-link>
        </div>
      </div>
      <div class="question" ref="questionElement">
        {{ questions[i] }}
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {IonContent, IonPage} from '@ionic/vue';
import {useRoute} from 'vue-router';
import {onMounted, ref} from "vue";
import router from "@/router";

// get language from route
const route = useRoute();
const lang = route.params.lang as "en" | "de";

//questions
const questions = ref([] as string[]);
const i = ref(0);
const questionElement = ref(null);
const showHelper = ref(false);
let lastClick = setTimeout(() => showHelper.value = true, 1000);

function nextQuestion() {
  // hide helper
  showHelper.value = false;
  clearTimeout(lastClick)
  lastClick = setTimeout(() => showHelper.value = true, 10000);

  // fade out
  if (questionElement.value) {
    (questionElement.value as HTMLElement).style.opacity = '0';
  }

  // fade in
  setTimeout(() => {
    i.value++;
    if (i.value >= questions.value.length) {
      i.value = 0;
    }
    if (questionElement.value) {
      (questionElement.value as HTMLElement).style.opacity = '1';
    }
  }, 500);
}

onMounted(() => {
  if (!['de', 'en'].includes(lang)) {
    router.replace({name: 'Home', params: {lang: 'de'}});
  }
  if (lang === 'de') {
    import('@/data/questions_de.json').then((data) => {
      questions.value = data.default.sort(() => Math.random() - 0.5);;
    });
    // set Content-Language via Vue
    document.documentElement.lang = 'de';

  } else {
    import('@/data/questions_en.json').then((data) => {
      questions.value = data.default.sort(() => Math.random() - 0.5);;
    });

    // set Content-Language via Vue
    document.documentElement.lang = 'en';
  }
});


</script>
<style>
.question {
  font-family: Montserrat, sans-serif;
  font-weight: 400;
  font-size: 1.2rem;

  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 90vw;

  color: var(--ion-color-primary);

  text-align: center;

  transition: 0.5s;
}

.content {
  height: 100vh;
  width: 100vw;
  padding: 5% 5%;
  cursor: pointer;
  transition: 0.5s;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.helper{
  opacity: 1;

  color: var(--ion-color-secondary);

  font-weight: 200;
  font-size: 1rem;

  text-align: center;
  transition: 2s;
}
.hidden{
  opacity: 0;
}
</style>
