from odoo import models, api
import logging

import base64
from os import path

logger = logging.getLogger(__name__)

class Company(models.Model):
  _inherit='res.company'

  # def _get_logo(self):
  #   logo_path =path.join(path.dirname(__file__), '../static/src/img/logo.png')
  #   logger.info('LOGO_PATH')
  #   logger.info(logo_path)
  #   return open(logo_path, 'rb') .read().encode('base64')

  @api.model
  def update_main_logo(self):
    logo_path = path.join(path.dirname(__file__), '../static/src/img/logo.png')
    logo_file = open(logo_path)
    content = base64.encodestring(logo_file.read())
    logo_file.close()
    logger.info('\nTODO: update comapny logo\n')

    # TODO: Update company logo
    # self.env.user.company_id.write({
    #   'logo': content
    # })
