<template>
  <div>
    <v-card>
      <v-form v-on:submit.prevent="filterMortgages">
        <v-container fluid>
          <v-row>
            <v-col cols="12" md="2">
              <v-select
                multiple
                clearable
                label="Банк"
                placeholder="Любой"
                :items="BANKS_DATA"
                v-model="filters.bank_name"
              >
                <template v-slot:selection="{ item, index }">
                  <span v-if="index === 0">
                    <span>{{ item }} </span>
                  </span>
                  <span v-if="index === 1" class="ml-1 grey--text caption"
                    >(+{{ filters.bank_name.length - 1 }})</span
                  >
                </template>
              </v-select>
            </v-col>

            <v-col cols="12" md="2">
              <v-select
                multiple
                clearable
                autocomplete
                label="Цель ипотеки"
                placeholder="Любая"
                :items="TARGET_CREDITS_DATA"
                v-model="filters.names_target_credits"
              >
                <template v-slot:selection="{ item, index }">
                  <span v-if="index === 0">
                    <span>{{ item }} </span>
                  </span>
                  <span v-if="index === 1" class="ml-1 grey--text caption"
                    >(+{{ filters.names_target_credits.length - 1 }})</span
                  >
                </template>
              </v-select>
            </v-col>

            <!--        <v-col cols="12" md="2">-->
            <!--          <v-text-field label="Банк" placeholder="Любой"></v-text-field>-->
            <!--        </v-col>-->

            <v-col cols="12" md="2">
              <v-text-field
                v-model.number="filters.property_value"
                type="number"
                label="Стоимость недвижимости, руб"
                placeholder="Любая"
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="2">
              <v-text-field
                v-model="filters.first_payment"
                type="number"
                label="Первоначальный взнос, %"
                placeholder="Любой"
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="1">
              <v-text-field
                v-model="filters.rate"
                type="number"
                label="Ставка"
                placeholder="Любая"
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="1">
              <v-text-field
                v-model="filters.time_credit"
                type="number"
                label="Срок"
                placeholder="Любой"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="12" md="1">
              <v-btn color="primary">+ ещё </v-btn>
            </v-col>

            <v-col cols="12" md="1">
              <v-btn color="primary" @click="clearFilter()"
                ><v-icon>mdi-cached</v-icon></v-btn
              >
            </v-col>

            <v-col cols="12" md="2">
              <v-btn color="primary" type="submit" width="150">Найти </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card>

    <v-spacer class="my-4"></v-spacer>

    <div class="text-center d-flex pb-4">
      <v-btn @click="all">Развернуть</v-btn>
      <!--      <div>{{ panel }}</div>-->
      <v-btn @click="none">Свернуть</v-btn>
    </div>

    <!--    <v-expansion-panels v-model="panel" multiple>-->
    <!--      <v-expansion-panel v-for="(item, i) in items" :key="i">-->
    <!--        <v-expansion-panel-header>-->
    <!--          <v-row no-gutters>-->
    <!--            <v-col cols="3">Header {{ item }}</v-col>-->
    <!--            <v-col cols="3" class="text&#45;&#45;secondary">Start and end dates</v-col>-->
    <!--            <v-col cols="3" class="text&#45;&#45;secondary">Start and end dates</v-col>-->
    <!--            <v-col cols="3" class="text&#45;&#45;secondary">Start and end dates</v-col>-->
    <!--          </v-row>-->
    <!--        </v-expansion-panel-header>-->

    <!--        <v-expansion-panel-content>-->
    <!--          <v-divider></v-divider>-->
    <!--          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do-->
    <!--          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad-->
    <!--          minim veniam, quis nostrud exercitation ullamco laboris nisi ut-->
    <!--          aliquip ex ea commodo consequat.-->
    <!--        </v-expansion-panel-content>-->
    <!--      </v-expansion-panel>-->
    <!--    </v-expansion-panels>-->

    <v-expansion-panels v-model="panel2" multiple>
      <v-expansion-panel
        class="no-transition"
        v-for="(mort, i) in MORTGAGES_DATA"
        :key="i"
      >
        <v-expansion-panel-header class="py-0">
          <v-container class="py-0" fill-height fluid>
            <v-row align="center" justify="center">
              <v-col cols="4" sm="2" md="1" lg="2">
                <div>
                  <v-img
                    :src="mort.bank.bank_logo"
                    max-width="120"
                    height="50"
                    contain
                  ></v-img>
                </div>
              </v-col>
              <v-col cols="8" sm="6" md="3" lg="2">
                <div class="mt-2">
                  <span class="grey--text text--darken-1 body-2"
                    >«{{ mort.bank.bank_name }}»
                  </span>
                </div>
                <div>
                  <span class="grey--text text--darken-3 body-2"
                    >«{{ mort.programs_name }}»
                  </span>
                </div>
              </v-col>
              <v-col cols="4" sm="6" md="2" lg="2">
                <div>
                  <span
                    class="grey--text text--darken-3 headline font-weight-black"
                    >{{ mort.rate }}%
                  </span>
                  <span class="text--secondary nowrap"
                    >{{ mort.first_payment }}% ПВ
                  </span>
                </div>
                <div></div>
              </v-col>
              <v-col cols="12" sm="6" md="4" lg="4" class="text--secondary">
                <div>
                  <span
                    class="grey--text text--darken-3 subtitle-1 font-weight-black"
                    >{{ mort.min_sum_credit | numCredit | toRUB }} -
                    {{ mort.max_sum_credit | numCredit | toRUB }}
                  </span>
                </div>
                <div>
                  <span class="text--secondary body-2"
                    >на срок от {{ mort.min_time_credit }} до
                    {{ mort.max_time_credit }} лет
                  </span>
                </div>
              </v-col>
              <v-col cols="6" sm="6" md="3" lg="2" class="text--secondary">
                <div>
                  <span class="text--secondary"
                    >возраст от {{ mort.min_borrower_age }} до
                    {{ mort.max_borrower_age }} лет
                  </span>
                </div>
                <!--                <div>-->
                <!--                  <span class="text&#45;&#45;secondary"-->
                <!--                    >на срок от {{ mort.min_time_credit }} до-->
                <!--                    {{ mort.max_time_credit }} лет</span-->
                <!--                  >-->
                <!--                </div>-->
              </v-col>
            </v-row>
          </v-container>
        </v-expansion-panel-header>

        <v-expansion-panel-content>
          <v-divider></v-divider>

          <div class="py-0" fill-height fluid>
            <v-row align="start" justify="center">
              <v-col cols="12" sm="6" md="4" lg="4" align="left">
                <v-list-item>
                  <v-list-item-content class="grey--text text--darken-1">
                    <v-list-item-title
                      class="mb-3 body-1 font-weight-bold grey--text text--darken-3"
                      >Условия ипотеки
                    </v-list-item-title>
                    <span class="caption"
                      >Цель:
                      <span v-for="(item, index) in mort.targets" :key="index">
                        {{ item.target_name
                        }}{{ mort.targets.length !== index + 1 ? "," : "" }}
                      </span>
                    </span>
                    <span class="caption"
                      >Программа: «{{ mort.programs_name }}»
                    </span>
                    <span class="caption"
                      >Первоначальный взнос: {{ mort.first_payment }}%
                    </span>
                    <span class="caption">Ставка: {{ mort.rate }}% </span>
                    <span class="caption"
                      >Ставка для зарплатников:
                      {{
                        !mort.rate_salary ? "-" : mort.rate_salary + "%"
                      }}</span
                    >
                    <span class="caption"
                      >Сумма: {{ mort.min_sum_credit | numCredit | toRUB }} -
                      {{ mort.max_sum_credit | numCredit | toRUB }}
                    </span>
                    <span class="caption"
                      >Срок: от {{ mort.min_time_credit }} до
                      {{ mort.max_time_credit }} лет
                    </span>
                    <span class="caption">
                      Занижение:
                      {{ mort.understatement_is_active ? "Да" : "Нет"
                      }}{{
                        mort.understatement_comment
                          ? ", " + mort.understatement_comment
                          : ""
                      }}
                    </span>
                    <span class="caption"
                      >Созаёмщики: {{ mort.co_borrowers }}
                    </span>
                    <span class="caption"
                      >Коммисия: {{ mort.commission }}
                    </span>
                    <span class="caption"
                      >Регистрация продавца:
                      {{ mort.seller_registration }}
                    </span>
                    <span class="caption"
                      >Экспресс выдача:
                      {{
                        mort.express_issue == "yes"
                          ? "Да"
                          : mort.express_issue == "no"
                          ? "Нет"
                          : ""
                      }}
                    </span>
                    <span class="caption"
                      >Включение детей в число собственников:
                      {{
                        mort.inclusion_children == "yes"
                          ? "Да"
                          : mort.inclusion_children == "no"
                          ? "Нет"
                          : ""
                      }}
                    </span>
                  </v-list-item-content>
                </v-list-item>
              </v-col>
              <v-col cols="12" sm="6" md="4" lg="4" align="left">
                <v-list-item>
                  <v-list-item-content
                    class="caption grey--text text--darken-1"
                  >
                    <v-list-item-title
                      class="mb-3 body-1 font-weight-bold grey--text text--darken-3"
                      >Условия ипотеки
                    </v-list-item-title>

                    <span class="caption">
                      Комната:
                      {{
                        mort.room == "yes"
                          ? "Да"
                          : mort.room == "no"
                          ? "Нет"
                          : ""
                      }}{{ mort.room_comment ? ", " + mort.room_comment : "" }}
                    </span>
                    <span class="caption">
                      Доля:
                      {{
                        mort.share == "yes"
                          ? "Да"
                          : mort.share == "no"
                          ? "Нет"
                          : ""
                      }}{{
                        mort.share_comment ? ", " + mort.share_comment : ""
                      }}
                    </span>
                    <span class="caption">
                      Частный дом:
                      {{
                        mort.private_house == "yes"
                          ? "Да"
                          : mort.private_house == "no"
                          ? "Нет"
                          : ""
                      }}{{
                        mort.private_comment ? ", " + mort.private_comment : ""
                      }}
                    </span>
                    <span class="caption">
                      Апартаменты:
                      {{
                        mort.apartments == "yes"
                          ? "Да"
                          : mort.apartments == "no"
                          ? "Нет"
                          : ""
                      }}{{
                        mort.apartments_comment
                          ? ", " + mort.apartments_comment
                          : ""
                      }}
                    </span>
                    <span class="caption">
                      Перепланировка:
                      {{
                        mort.redevelopment == "yes"
                          ? "Да"
                          : mort.redevelopment == "no"
                          ? "Нет"
                          : ""
                      }}{{
                        mort.redevelopment_comment
                          ? ", " + mort.redevelopment_comment
                          : ""
                      }}
                    </span>
                    <p class="caption mb-1">
                      Перекрытия:<span class="grey--text text--darken-3">
                        {{ mort.overlap }}
                      </span>
                    </p>
                    <p class="caption mb-1">
                      Этажность:<span class="grey--text text--darken-3">
                        {{ mort.storeys }}
                      </span>
                    </p>
                    <p class="caption mb-1">
                      Износ жилья:<span class="grey--text text--darken-3">
                        {{ mort.housing_wear }}
                      </span>
                    </p>
                    <p class="caption mb-1">
                      Технические документы:
                      <span class="grey--text text--darken-3">
                        {{ mort.req_tech_docs }}
                      </span>
                    </p>
                  </v-list-item-content>
                </v-list-item>
              </v-col>
              <v-col cols="12" sm="6" md="4" lg="4" align="left">
                <v-list-item>
                  <v-list-item-content class="grey--text text--darken-1">
                    <v-list-item-title
                      class="mb-3 body-1 font-weight-bold grey--text text--darken-3"
                      >Условия ипотеки</v-list-item-title
                    >
                    <span class="caption"
                      >Программа: «{{ mort.programs_name }}»
                    </span>
                    <span class="caption"
                      >Первоначальный взнос: {{ mort.first_payment }}%
                    </span>
                    <span class="caption">Ставка: {{ mort.rate }}%</span>
                    <span class="caption"
                      >Сумма: {{ mort.min_sum_credit | numCredit | toRUB }} -
                      {{ mort.max_sum_credit | numCredit | toRUB }}
                    </span>
                    <span class="caption"
                      >Срок: от {{ mort.min_time_credit }} до
                      {{ mort.max_time_credit }} лет
                    </span>
                  </v-list-item-content>
                </v-list-item>
              </v-col>
            </v-row>
          </div>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import { getAPI } from "../api/mortgages/axios-mortgages";
import { mapState, mapMutations, mapActions } from "vuex";

export default {
  name: "MortgagesListComp",

  data() {
    return {
      url: "api/v1/mortgages/all/",
      filters: [],
      selectTargets: ["Foo", "Bar", "Fizz", "Buzz"],
      // panel: [],
      panel2: [],
      items: 5,
      value: null
    };
  },
  computed: {
    ...mapState("mortgages", [
      "MORTGAGES_DATA",
      "BANKS_DATA",
      "TARGET_CREDITS_DATA"
    ])
  },
  methods: {
    ...mapMutations("mortgages", [
      "SET_UPDATE_MORTGAGES_DATA",
      "SET_UPDATE_BANKS_DATA",
      "SET_UPDATE_TARGET_CREDITS_DATA"
    ]),
    ...mapActions("mortgages", [
      "FETCH_MORTGAGES",
      "FETCH_BANKS",
      "FETCH_TARGET_CREDITS"
    ]),

    // Create an array the length of our items
    // with all values as true
    all() {
      this.panel2 = [...Array(this.MORTGAGES_DATA.length).keys()].map(
        (k, i) => i
      );
    },
    // Reset the panel
    none() {
      this.panel2 = [];
    },
    clearFilter() {
      this.filters = [];
      this.FETCH_MORTGAGES();
      return this.filters;
    },
    filterMortgages() {
      const params = new URLSearchParams();
      for (let item in this.filters) {
        if (this.filters[item] !== "") {
          params.append(item, this.filters[item]);
        }
        // console.log(this.filters[item]);
      }
      // this.fetchMortgages(this.url, params);
      this.FETCH_MORTGAGES(params);
      // console.log(this.BANKS_DATA);
    }
  },
  created() {
    this.FETCH_MORTGAGES();
    this.FETCH_BANKS();
    this.FETCH_TARGET_CREDITS();
  },
  mounted() {},
  filters: {
    numCredit(value) {
      return new Intl.NumberFormat().format(value);
    },
    toRUB(value) {
      return `${value.toLocaleString()} ₽`;
    }
  }
};
</script>

<style scoped>
/* Убираем анимацию у v-expansion-panel (ТОРМОЗИТ сильно!)*/
.no-transition {
  transition: none !important;
}
.expand-transition-leave-active,
.expand-transition-enter-active {
  transition: none !important;
}
.nowrap {
  white-space: nowrap;
}
</style>
