/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';

export class AMSAutorizationListController extends ListController {
   setup() {
       super.setup();
   }

   /* el modelo de abajo es en el que se define que vista es la que se quiere abrir */

   OpenCreateAutorizationWizard() {
       this.actionService.doAction({
          type: 'ir.actions.act_window',
          res_model: 'ams.create.autorization.wizard',
          name:'Open Wizard',
          view_mode: 'form',
          view_type: 'form',
          views: [[false, 'form']],
          target: 'new',
          res_id: false,
      });
   }
}

/* esto se copia igual, solo se le agrega el nombre de la clase al Controller*/

const viewRegistry = registry.category("views");

export const AutorizationListController = {
    ...listView,
    Controller: AMSAutorizationListController,
};

/* aca se agrega un identificador de la classe js que hara la referencia a esta clase y el controlador */

viewRegistry.add("odoo_autorization_controller", AutorizationListController);